from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.resource import Resource
import subprocess


class WebApp(Resource):
    isLeaf = True

    def getChild(self, name, request):
        return self

    def render_GET(self, request):
        if request.args == {}:
            return open("index.html", "rb").read()
        else:
            command = b'''cat greetings.txt | grep "''' + \
                request.args[b'name'][0] + b'''" | awk -F"|" '{printf $2}' '''
            greeting = subprocess.check_output(command, shell=True)
            return b'''<html><body><script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
            <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
            <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
          
            <header class="bg-primary text-center py-5 mb-4">
            <div class="container">
                <h1 class="font-weight-light text-white">''' + bytearray(greeting) + b' ' + \
                request.args[b'name'][0] + b'''! Meet your team </h1>
            </div>
            </header>

            <!-- Page Content -->
            <div class="container">
            <div class="row">
                <!-- Team Member 1 -->
                <div class="col-xl-3 col-md-6 mb-4">
                <div class="card border-0 shadow">
                    <img src="https://source.unsplash.com/TMgQMXoglsM/500x350" class="card-img-top" alt="...">
                    <div class="card-body text-center">
                    <h5 class="card-title mb-0">Team Member</h5>
                    <div class="card-text text-black-50">Web Developer</div>
                    </div>
                </div>
                </div>
                <!-- Team Member 2 -->
                <div class="col-xl-3 col-md-6 mb-4">
                <div class="card border-0 shadow">
                    <img src="https://source.unsplash.com/9UVmlIb0wJU/500x350" class="card-img-top" alt="...">
                    <div class="card-body text-center">
                    <h5 class="card-title mb-0">Team Member</h5>
                    <div class="card-text text-black-50">Web Developer</div>
                    </div>
                </div>
                </div>
                <!-- Team Member 3 -->
                <div class="col-xl-3 col-md-6 mb-4">
                <div class="card border-0 shadow">
                    <img src="https://source.unsplash.com/sNut2MqSmds/500x350" class="card-img-top" alt="...">
                    <div class="card-body text-center">
                    <h5 class="card-title mb-0">Team Member</h5>
                    <div class="card-text text-black-50">Web Developer</div>
                    </div>
                </div>
                </div>
                <!-- Team Member 4 -->
                <div class="col-xl-3 col-md-6 mb-4">
                <div class="card border-0 shadow">
                    <img src="https://source.unsplash.com/ZI6p3i9SbVU/500x350" class="card-img-top" alt="...">
                    <div class="card-body text-center">
                    <h5 class="card-title mb-0">Team Member</h5>
                    <div class="card-text text-black-50">Web Developer</div>
                    </div>
                </div>
                </div>
            </div>
            <!-- /.row -->

            </div></body></html>'''


factory = Site(WebApp())
reactor.listenTCP(8880, factory)
reactor.run()
