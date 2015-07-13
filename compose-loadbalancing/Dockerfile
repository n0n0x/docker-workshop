FROM    node

MAINTAINER Santiago del Castillo

# Provides cached layer for node_modules
ADD app /app

WORKDIR /app
RUN npm install

# Expose port
EXPOSE  8080

CMD ["node", "index.js"]
