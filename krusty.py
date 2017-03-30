#!/usr/bin/env python3.6
from application import controller as krusty

# MAIN
if __name__ == '__main__':
    app = krusty.Controller('800x600+100+100', debug=True)
    app.run()
