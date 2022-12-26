FROM gcc

WORKDIR app/

COPY . .

RUN g++ -o day_four main.cpp

CMD ["./day_four", "resources/input.txt"]