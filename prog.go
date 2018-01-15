package main

import "fmt"

type rand uint32

func (r *rand) mix(v uint32) {
	*r = ((*r << 5) + *r) + rand(v)
}

func (r *rand) rand() uint32 {
	mx := rand(int32(*r)>>31) & 0xa8888eef
	*r = *r<<1 ^ mx
	return uint32(*r)
}

func hex(v uint32) string {
	var b []byte
	for v != 0 {
		if x := byte(v & 0xf); x < 10 {
			b = append(b, '0'+x)
		} else {
			b = append(b, 'a'+x-10)
		}
		v >>= 4
	}
	return string(b)
}

func RaceCondition() string {
	var r rand
	for i := 0; i < 1000; i++ {
		ch := make(chan uint32, 2)
		start := make(chan bool)
		go func() {
			<-start
			ch <- 1
		}()
		go func() {
			<-start
			ch <- 2
		}()
		close(start)
		r.mix(<-ch)
	}
	return hex(r.rand())
}

func Select() string {
	var r rand

	ch := make(chan bool)
	close(ch)
	for i := 0; i < 1000; i++ {
		select {
		case <-ch:
			r.mix(1)
		case <-ch:
			r.mix(2)
		}
	}
	return hex(r.rand())
}

func main() {
	fmt.Println("RaceCondition: ", RaceCondition())
	fmt.Println("Select:", Select())
}
