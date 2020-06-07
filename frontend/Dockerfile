FROM node:10-stretch-slim as nodeimage
WORKDIR /usr/src/app
COPY . .
RUN npm install
RUN npm run build
FROM nginx
COPY nginx.conf /etc/nginx/nginx.conf
COPY --from=nodeimage /usr/src/app/build /usr/share/nginx/html
