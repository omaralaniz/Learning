package main

import (
	"playground/httpd/handler"

	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()
	r.GET("/ping", handler.AboutGet())
	r.Run() // listen and serve on 0.0.0.0:8080
}
