# CMDBuild

Python library for interacting with CMDBuild REST API.

## Install and use

1.  Setup a Python 3 virtual environment

        $ virtualenv -p python3 .venv
        $ . .venv/bin/activate
        $ pip install -r requirements.txt

2.  Install the module

        $ pip install -e .

3.  Use it

    ~~~.py
    from cmdbuild import CMDBuild

    if __name__ == '__main__':

        host = 'cmdbuild.antani.it'
        port = 443
        tls = True
        tls_verify = False
        username = 'lmascetti'
        password = 'QW50YW5pLCBibGluZGEgbGEgc3VwZXJjYXp6b2xhIHByZW1hdHVyYXRhIGNvbiBkb3BwaW8gc2NhcHBlbGxhbWVudG8gYSBkZXN0cmE/'

        with CMDBuild(host, port, tls, tls_verify, username=username, password=password) as cli:
            for iface in cli.network_interface.list():
                print(iface)
    ~~~

## References

* [CMDBuild - Webservice Manual](https://www.cmdbuild.org/file/manuali/webservice-manual-in-english)
