import httplib2
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run_flow
from googleapiclient import discovery
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('BLOG_API_KEY')

class BlogApi:

    # Start the OAuth flow to retrieve credentials
    def authorize_credentials(self):
        CLIENT_SECRET = 'client_secret.json'
        SCOPE = 'https://www.googleapis.com/auth/blogger'
        STORAGE = Storage('credentials.storage')
        # Fetch credentials from storage
        credentials = STORAGE.get()
        # If the credentials doesn't exist in the storage location then run the flow
        if credentials is None or credentials.invalid:
            flow = flow_from_clientsecrets(CLIENT_SECRET, scope=SCOPE)
            http = httplib2.Http()
            credentials = run_flow(flow, STORAGE, http=http)
        return credentials

    # print(credentials)
    def getBloggerService(self):
        credentials = self.authorize_credentials()
        http = credentials.authorize(httplib2.Http())
        discoveryUrl = ('https://blogger.googleapis.com/$discovery/rest?version=v3')
        service = discovery.build('blogger', 'v3', http=http, discoveryServiceUrl=discoveryUrl)
        return service

    def postToBlogger(self, blog_id, title, body):
        payload = {
            "title": title,
            "content": body,           
        }
        service = self.getBloggerService()
        post=service.posts()
        insert=post.insert(blogId= blog_id,body=payload).execute()
        print("Done post!")
        return insert
    
    def getBlog(self, blog_id):
        http = httplib2.Http()
        response = http.request(f'https://www.googleapis.com/blogger/v3/blogs/{blog_id}?key={API_KEY}', 'GET')
        return response


    

    
