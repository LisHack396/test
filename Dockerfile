FROM node:18-alpine

USER root

ARG FLOWISE_PATH=/usr/local/lib/node_modules/flowise

ARG BASE_PATH=/root/.flowise

ARG DATABASE_PATH=$BASE_PATH

ARG APIKEY_PATH=$BASE_PATH

ARG SECRETKEY_PATH=$BASE_PATH

ARG LOG_PATH=$BASE_PATH

ARG BLOB_STORAGE_PATH=$BASE_PATH/BLOB_STORAGE_PATH

#Install dependencies
RUN apk add --no cache git python3 py3-pip make g++ build-base cairo-dev pango-dev chromium

ENV PUPPETEER_SKIP_DOWNLOAD=true

ENV PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium-browser

#Install Flowise globally
RUN npm install -g flowise

#Configure Flowise directory using the ARG
RUN mkdir -p $LOG_PATH $FLOWISE_PATH/uploads && chmod -R 777 $LOG_PATH $FLOWISE_PATH