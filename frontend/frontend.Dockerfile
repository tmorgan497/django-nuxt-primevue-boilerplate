# frontend/frontend.Dockerfile

FROM node:18-alpine AS dev
ENV HOST 0.0.0.0

WORKDIR /code/frontend

RUN apk --no-cache add curl

COPY package.json ./
RUN yarn install
