FROM gcc

WORKDIR app/

COPY . .

RUN gcc main.c

CMD ["./a.out", "resources/input.txt"]