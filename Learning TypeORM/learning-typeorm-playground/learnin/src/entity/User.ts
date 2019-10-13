import {Entity, PrimaryGeneratedColumn, Column, BeforeInsert, BaseEntity} from "typeorm";
import * as uuidv4 from "uuid/v4";

@Entity("users")
export class User extends BaseEntity {

    @PrimaryGeneratedColumn("uuid") id: string;
 
    @Column("char", {length: 255})
    firstName: string;

    @Column("char", {length: 255})
    lastName: string;

    @Column()
    age: number;

    @Column("char", {length: 255}) email: string;

    @Column("text") password: string;

    @BeforeInsert()
    addId(){
        this.id = uuidv4();
    }

}
