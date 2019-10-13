import { ResolverMap } from "./types/graphql-utils";
import * as bcrypt from 'bcryptjs';
import { User } from "./entity/User";

export const resolvers: ResolverMap = {
  Query: {
    hello: (_, { name }: GQL.IHelloOnQueryArguments) => `Hello ${name || 'Loser'}`,
  },

  Mutation: {
    register: async (_, {firstName, lastName, age, email, password }: GQL.IRegisterOnMutationArguments) => {
      const hashPassword = await bcrypt.hash(password, 10);
      const user = User.create({
        firstName,
        lastName,
        age,
        email,
        password: hashPassword
      });

      await user.save();
      
      return true;
    }
  }

};