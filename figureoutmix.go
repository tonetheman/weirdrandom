package main

import "fmt"

type rand uint32

func (r *rand) mix(v uint32) {
	// the rand is a typecast
	*r = ((*r << 5) + *r) + rand(v)
}

func (r *rand) rand() uint32 {
	fmt.Println("rand() is called")
	// this is a typecast here no func call
	mx := rand(int32(*r)>>31) & 0xa8888eef
	*r = *r<<1 ^ mx
	return uint32(*r)
}

func main() {
	var r rand
	for i := 0; i < 10; i++ {
		r.mix(uint32(i))
	}
	fmt.Println(r.rand())
}
