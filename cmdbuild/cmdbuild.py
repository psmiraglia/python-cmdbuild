'''
Copyright 2023 Paolo Smiraglia <paolo.smiraglia@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

from restfly.session import APISession


class CMDBuild(APISession):
    def __init__(self, host, port=443, tls=True, tls_verify=True, **kwargs):
        # configure TLS
        schema = 'https'
        if not tls:
            schema = 'http'
        self._ssl_verify = tls_verify

        # build the API base URL
        self._url = f'{schema}://{host}:{port}/cmdbuild/services/rest/v3'

        # init the class
        super(CMDBuild, self).__init__(**kwargs)

    def _authenticate(self, **kwargs):
        headers = {'content-type': 'application/json'}
        params = {'scope': 'service', 'returnId': True}

        username = kwargs.pop('username', None)
        password = kwargs.pop('password', None)

        if username and password:
            data = {'username': username, 'password': password}
            _resp = self.post('sessions',
                              headers=headers,
                              params=params,
                              json=data)
            try:
                resp = _resp.json()
                if resp['success']:
                    session_id = resp['data']['_id']
                    self._session.headers.update({
                        'cmdbuild-authorization': session_id
                    })
                    print('(*) Logged in')
                else:
                    print('(!) Authentication failed')
            except Exception as e:
                print(f'(!) Error: {e}')
        else:
            print('(!) Error: missing credentials')

    def _deauthenticate(self):
        if 'cmdbuild-authorization' in self._session.headers:
            self._session.headers.pop('cmdbuild-authorization')
            print('(*) Logged out')
