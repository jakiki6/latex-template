align 16
global native_rdtsc
native_rdtsc:
	push rbx
	xor rax, rax
	cpuid
	pop rbx

	rdtsc
	shl rdx, 32
	or rax, rdx

        push rax
	push rbx
	xor rax, rax
	cpuid
	pop rbx
	pop rax

	ret

align 64
global native_rdseed
native_rdseed:
	rdseed rax
	ret
