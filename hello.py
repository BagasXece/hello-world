class Hello_World:
    def __init__(self) -> None:
        pass
    
    def __str__(self) -> str:
        return f"Hello , World!"
    
    @classmethod
    def main(cls) -> None:
        hello = cls()
        print(hello)
        
if __name__ == "__main__":
    Hello_World.main()

