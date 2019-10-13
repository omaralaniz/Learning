interface UserInterface{
  name: string;
  email: string;
  age: number;
  register();
  payInvoice();
}

class User implements UserInterface{
  name: string;
  email: string;
  age: number;
  
  constructor(name: string, email: string, age: number) {
    this.name = name;
    this.email = email;
    this.age = age;

    console.log(`User created: ${this.name}`);
    
  }

  register():void {
    console.log(`${this.name} is now registered!`);
    
  }

  payInvoice():void{
    console.log(`${this.name} paid invoice.`);
    
  }
}

let omar = new User('Omar Alaniz', 'omar.alaniz021@gmal.com', 23);

omar.register();
// console.log(omar.age);


class Member extends User {
  id: number;
  
  constructor(id: number, name: string, email: string, age: number){
    super(name, email, age);
    this.id = id;
  }

  payInvoice(){
    super.payInvoice();
  }
}

let mike: User = new Member(1, 'Mike Smith', 'mike@aol.com', 32);
mike.payInvoice();