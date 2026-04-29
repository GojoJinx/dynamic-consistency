type Node struct {
	id    int
	state int
}
func createNodes(n int) []Node {
	nodes := make([]Node, n)
	for i := 0; i < n; i++ {
		nodes[i] = Node{id: i + 1, state: 0}
	}
	return nodes
}
func writeOperation(primary *Node) {
	update := rand.Intn(50) + 1
	primary.state += update
	fmt.Println("Primary update value", update)
}
func replicate(primary Node, replicas []Node) []Node {
	for i := range replicas {
		delay := rand.Intn(100) + 50
		time.Sleep(time.Millisecond * time.Duration(delay))
		replicas[i].state = primary.state
		fmt.Println("Replica", replicas[i].id, "sync delay", delay)
	}
	return replicas
}
func readStates(primary Node, replicas []Node) {
	fmt.Println("Primary state", primary.state)
	for _, r := range replicas {
		fmt.Println("Replica", r.id, "state", r.state)
	}
}
func runCycle(primary *Node, replicas []Node, cycle int) []Node {
	fmt.Println("Cycle", cycle)
	writeOperation(primary)
	replicas = replicate(*primary, replicas)
	readStates(*primary, replicas)
	return replicas
}
func main() {
	rand.Seed(time.Now().UnixNano())
	primary := Node{id: 0, state: 0}
	replicas := createNodes(5)
	for i := 1; i <= 5; i++ {
		replicas = runCycle(&primary, replicas, i)
	}
}
