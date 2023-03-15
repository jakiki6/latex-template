TARGETS = test_rdseed

all: $(TARGETS)

test_rdseed: test_rdseed.o native.o
	gcc -o $@ $^

%.o: %.c
	gcc -c -O2 -o $@ $<

%.o: %.asm
	nasm -f elf64 -o $@ $<

clean:
	rm -f $(TARGETS) *.o

.PHONY: all run clean
