FROM node:lts-alpine

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

# RUN npm install @vue/cli@4.5.13 -g
RUN npm install -g @vue/cli@5.0.8

COPY package.json .
COPY package-lock.json .
RUN npm install --force

CMD ["npm", "run", "serve"]