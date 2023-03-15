#include <stdio.h>
#include <stdint.h>

#include "native.h"

#define ROUNDS 1000

int main() {
    uint64_t base_cycles = 0;
    uint64_t test_cycles = 0;

    for (int i = 0; i < ROUNDS; i++) {
        uint64_t start = native_rdtsc();
        native_ret(); 
        uint64_t delta = native_rdtsc() - start;
        base_cycles += delta;
    }

    for (int i = 0; i < ROUNDS; i++) {
        uint64_t start = native_rdtsc();
        native_rdseed();
	uint64_t delta = native_rdtsc() - start;
	test_cycles += delta;
    }

    printf("average cycles/inst: %lu\n", (test_cycles - base_cycles) / ROUNDS);
}
