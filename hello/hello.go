package hello

import (
    "fmt"
    "net/http"
)

func init() {
    http.HandleFunc("/hello/v1/service", handler)
}

func handler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprint(w, "Hello, world!")
}
