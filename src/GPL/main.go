package main

import (
	"os"

	"GPL/repl"
)

func main() {

	if len(os.Args) > 2 {
		path := os.Args[1]
		repl.PrintAst(path, os.Stdout)
		return
	}

	if len(os.Args) > 1 {
		path := os.Args[1]
		repl.ExecuteFile(path, os.Stdout)
		return
	}
}
