from unittest import case


class MathLib:

    @classmethod
    def execute(self, mathRequest):
        oper = mathRequest.get_oper()
        ope1 = mathRequest.get_ope1()
        ope2 = mathRequest.get_ope2()

        match oper:
             case 'add':
                 mathRequest.set_res(ope1 + ope2)
             case 'sub':
                 mathRequest.set_res(ope1 - ope2)
             case 'mul':
                 mathRequest.set_res(ope1 * ope2)
             case 'div':
                 mathRequest.set_res(ope1 / ope2)
             case 'pow':
                 mathRequest.set_res(ope1 ** ope2)
             case 'root':
                 mathRequest.set_res(ope1 ** (1/ope2))


#Autre solution

        #if(oper == 'add'):
         #   res = ope1 + ope2
          #  mathRequest.set_res(res)

        #if(oper == 'sub'):
        #   res = ope1 - ope2
         #   mathRequest.set_res(res)

        #if(oper == 'mul'):
         #   res = ope1 * ope2
          #  mathRequest.set_res(res)

        #if(oper == 'div'):
         #   res = ope1 / ope2
          #  mathRequest.set_res(res)

        #if(oper == 'pow'):
        #    res = ope1 ** ope2
         #   mathRequest.set_res(res)

        #if(oper == 'root'):
         #   res = ope1 ** (1/ope2)
          #  mathRequest.set_res(res)