align 16
global native_rdtsc
native_rdtsc:
        push rax
	push rbx
	push rcx
	push rdx
	xor rax, rax
	cpuid
        pop rdx
	pop rcx
	pop rbx
	pop rax

	rdtsc
	shl rdx, 32
	or rax, rdx

        push rax
	push rbx
	push rcx
	push rdx
	xor rax, rax
	cpuid
	pop rdx
	pop rcx
	pop rbx
	pop rax

	ret

align 16
global native_rdseed
native_rdseed:
	rdseed rax
	ret

align 16
global native_ret
native_ret:
	ret
