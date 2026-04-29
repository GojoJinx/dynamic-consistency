import (
	"fmt"
	"math/rand"
	"time"
)

type Node struct {
	id    int
	state int
	load  int
}

func createNodes(n int) []Node {
	nodes := make([]Node, n)
	for i := 0; i < n; i++ {
		nodes[i] = Node{id: i + 1, state: 0, load: rand.Intn(40)}
	}
	return nodes
}

func updatePrimary(primary *Node) {
	val := rand.Intn(60) + 1
	primary.state += val
	fmt.Println("Primary update", val)
}

func adaptiveSync(primary Node, nodes []Node) []Node {
	for i := range nodes {
		base := rand.Intn(70) + 30
		adjust := nodes[i].load / 2
		delay := base + adjust
		time.Sleep(time.Millisecond * time.Duration(delay))
		nodes[i].state = primary.state
		fmt.Println("Node", nodes[i].id, "sync", delay)
	}
	return nodes
}

func observe(primary Node, nodes []Node) {
	fmt.Println("Primary", primary.state)
	for _, n := range nodes {
		fmt.Println("Node", n.id, n.state)
	}
}

func process(primary *Node, nodes []Node, c int) []Node {
	fmt.Println("Cycle", c)
	updatePrimary(primary)
	nodes = adaptiveSync(*primary, nodes)
	observe(*primary, nodes)
	return nodes
}

func main() {
	rand.Seed(time.Now().UnixNano())
	primary := Node{id: 0, state: 0, load: 0}
	nodes := createNodes(5)

	for i := 1; i <= 6; i++ {
		nodes = process(&primary, nodes, i)
	}

	fmt.Println("Adaptive replication complete")
}
