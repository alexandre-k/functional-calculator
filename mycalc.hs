import qualified Data.Map as M


data Operand = Integer
data Operator = (+) | (-) | (*) | (/)
data Computation = Operand

operators :: String -> Operator
operators = undefined

enterNum :: String -> IO () -> Operand
enterNum = do
  putStrLn "> "
  value <- getLine
  convertedValue <- read value
  return convertedValue

enterOp :: IO () -> String
enterOp = undefined


compute :: (Operand, Operand) -> Operator -> Computation
compute = undefined


calculator :: Integer -> Integer -> String -> IO ()
calculator = undefined


main :: IO ()
main = undefined
  
