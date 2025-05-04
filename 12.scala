/*
Installing Scala:

sudo apt update
sudo apt install openjdk-11-jdk -y
java -version

sudo apt install scala -y
*/

object HelloWorld {
  def main(args: Array[String]){
    println("Hello World!")
  }
}

/* 
Compiling program

Save as HelloWorld.scala

Run: scalac HelloWorld.scala
scala HelloWorld
*/
