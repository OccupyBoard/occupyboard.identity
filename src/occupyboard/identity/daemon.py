# Copyright 2012, TheOccupyBoard Team http://blog.theoccupyboard.com
# All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# import stdlibs
import os
# import thirdparty libs
import bottle as web
# import local libs


DEV=True
web.debug(DEV)

@web.route('/public/:path')
def static(path):
    web.static_file(path,root='/public')

@web.route('/.*')
def fallback():
    web.abort(404, "Not Found")

def main():
    web.run(reloader=DEV)

if __name__=="__main__":
    main()
