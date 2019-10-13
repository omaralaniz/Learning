# Understanding T_TypeOrm

## Basic Built-ins

### find()

has basic uses: `select`, `relations`,  `where`, `join`, `order`.

* #### `select`

  displays properties of the main object which should be implemented.

  ```typescript
  userRepository.find({ select: ["firstName", "lastName"] });
  ```

  Returns the columns in the object specified.  

* #### `relations`

* #### `where`  

  `where` attribute allows to specify certain conditions to be queried. Here is a quick example:
  
  ```typescript
  userRepository.find({ where: { firstName: "Timber", lastName: "Saw" } });
  ```
  
  the return type of this function is an `Object`. In the above example, returns the object where the `firstName` equals "Timber" and `lasatName`  equals "Saw". It looks for a tuple where these two columns meet the conditions. 
  
  Another option for using `where` is using it with as an OR operator. Here is an example:
  
  ```typescript
  userRepository.find({
    where: [
      { firstName: "Timber", lastName: "Saw" }, //First User
      { firstName: "Stan", lastName: "Lee" } //Second User
    ]
  });
  ```
  
  In this example, the function will look for a tuple the meets the condition the satisfies the information of `First User` or `Second User`. 
  
  
  
  Using an example from a group project that I was part of MapSpace we had this function:
  
  
  
  
  
  
  
  
  
  