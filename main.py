# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START app]
from flask import Flask
from gcloud import datastore
import sys
import urllib2
import json
from oauth2client.client import GoogleCredentials
import httplib2
from oauth2client.contrib.appengine import AppAssertionCredentials

app = Flask(__name__)


@app.route('/')
def hello():

    credentials = AppAssertionCredentials([])
    client = datastore.Client(project = 'mq-cloud-prototyping-3', credentials = credentials)
    sys.stdout.write(credentials.to_json())
    
    query = client.query(kind='Person')
    res = query.fetch()
    all = dict(res)
    sys.stdout.write(str(all))
    
    return credentials.to_json()

    try :        
    	
    	token = ''

    	#ouath
        O_AUTH_EMAIL_SCOPE = 'https://www.googleapis.com/auth/userinfo.email'

        credentials = GoogleCredentials.get_application_default()
        if credentials.create_scoped_required():
	        credentials = credentials.create_scoped(PUBSUB_SCOPES)
        http = httplib2.Http()
        credentials.authorize(http)

        cl = discovery.build('pubsub', 'v1', http=http)
        return credentials.to_json()

        credentials = GoogleCredentials.get_application_default()
        credentials = credentials.create_scoped([O_AUTH_EMAIL_SCOPE])
      	http = httplib2.Http()
    	credentials.authorize(http)
        return credentials.to_json()
	    #if not http:
	    #    http = httplib2.Http()
	    #credentials.authorize(http)

    	#temp hardcoded token
        #token = 'ya29.CjjlAlrvqUwXrujCnJuqa08HTtmNilyP7K1GGrHQ40Gt489H6NGT9WQAxEL92OSQ6anGYeFPRcvI4g'

        



        tokenBearer = 'Bearer %s' % token
        url = 'https://admin-dot-mq-vouchers.appspot.com/api/communities/mtv1/campaigns?page=0&size=1000&sorting=campaignName,ASC'
        req = urllib2.Request(url, headers = {'Content-Type': 'application/json', 'Authorization' : tokenBearer})
        f = urllib2.urlopen(req)
        response = f.read()
        sys.stdout.write(str(response))
        respjson = json.loads(response)
        
        f.close()
        #respjson = '3333'
        #sys.stdout.write(str(all))
        return str(response)
    except urllib2.HTTPError, error:
    	return ('get failed %s' % error)



    """Return a friendly HTTP greeting."""
    


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END app]
