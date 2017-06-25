from psycopg2 import pool


connection_pool=pool.SimpleConnection(1,10,
                                      database="learning",
                                      user="progres",
                                      host="localhost")

class ConnectionFromPool:
    def __init__(self):
        self.connection=None


    def __enter__(self):
        self.connection=connection_pool.getconn()
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection_pool.putconn(self.connection)