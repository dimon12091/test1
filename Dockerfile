FROM nginx

RUN apt-get update -y && \
    apt install htop && \
    apt-get install -y python3-pip python3-dev libpq-dev gcc && \
    pip3 install psycopg2-binary && \
    pip3 install psycopg2 && \
    mkdir /scripts


COPY ./py-connect-postgress /scripts

CMD ["sh", "-c", "python3 /scripts/main.py ; nginx -g 'daemon off;'"]