#!/usr/bin/env python3.6
from application.controller import Controller

# MAIN
if __name__ == '__main__':
    app = Controller('800x600+100+100', debug=True)
    app.run()
