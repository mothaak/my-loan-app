FROM node:18
WORKDIR /frontend
COPY package*.json ./
RUN npm install
ENV DANGEROUSLY_DISABLE_HOST_CHECK=true
COPY . .
CMD [ "npm", "start", "--port=3000" ]
