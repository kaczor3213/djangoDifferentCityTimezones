FROM python:3.8-slim

ENV ENVIRONMENT docker
ENV NAME example
ENV HOME /home/$NAME
ENV APP /home/$NAME/app

RUN useradd --create-home --home-dir $HOME -u 1000 $NAME \
    && mkdir -p $HOME \
    && chown -R $NAME:$NAME $HOME

RUN ["pip", "install", "pipenv"]

USER $NAME
COPY --chown=$NAME ./src $APP
WORKDIR $APP

RUN ["pipenv", "sync"]
CMD ["/bin/bash", "entrypoint.sh"]