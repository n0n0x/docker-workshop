FROM    node

MAINTAINER Santiago del Castillo

ADD app /app

WORKDIR /app

RUN npm install

# Expose port
EXPOSE  8080

CMD ["node", "index.js"]
