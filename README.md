docker-bones
============

Docker, Gunicorn, Redis, Memcached, and PostgreSQL.

1. Grab the docker client and daemon 

    ```bash
    $ brew install boot2docker
    $ brew install docker
    ```

2. Now start the docker daemon

    ```bash
    $ boot2docker init
    $ boot2docker up
    ```

3. Fetch images & start service containers

    ```bash
    $ ./start.sh
    ```

4. Test that the web app is working

    ```bash
    $ ./test.sh
    {
        "hits": "1"
    }
    ```
