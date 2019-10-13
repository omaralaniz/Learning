package handler

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func AboutGet() gin.HandlerFunc {
	// this allows to pass in parameters
	return func(c *gin.Context) {
		c.JSON(http.StatusOK, map[string]string{
			"omar": "sweet",
		})
	}
}
