FROM node:22-alpine
WORKDIR /app

ARG VITE_API_BASE_URL
ENV VITE_API_BASE_URL=$VITE_API_BASE_URL


COPY package.json .

RUN npm install -g serve
RUN npm install
COPY . .
RUN npm run build
CMD ["serve", "-s", "-l", "5173", "./dist"]