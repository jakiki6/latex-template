#include <stdio.h>
#include <stdint.h>

#include "native.h"

#define ROUNDS 0x100000

int main() {
    uint64_t test_cycles = 0;

    for (int i = 0; i < ROUNDS; i++) {
        uint64_t start = native_rdtsc();
        native_rdseed();
	uint64_t delta = native_rdtsc() - start;

	if (delta < 10000) test_cycles += delta;
    }

    printf("average cycles/inst: %f\n", (double) test_cycles / ROUNDS);
}
