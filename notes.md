# Seminar ProgLLM Notizen

## Problems
- Obsolete libraries/APIs/dependencies
    - remedy: ask for the version!
    - very annoying: it even had old versions of the openai apis...
- "This task would require a team of developers ..." / "This taks is highly complex ..." / "I can provide a basic implementation which needs to be extended"
    - remedy: Prompt: "You are a team of experienced [XYZ-] engineers".
- Systems design can be overwhelming, as it will present many differen technologies which you may not yet know.
- Configurations are always the same! Especially when you design microservices, it will always use the same ports.
- The interfaces which are built are not actually used! -> you have to know how apis/sockets/etc work
- Some terms like "OpenAI Function Calling" refer to a specific concept, but are not recognized as such, and interpreted as "functions"
- Gives recommendations like "this is not for production setup, you should use XX"

## Insights
- It still makes sense to learn new technologies
    - If you already know the technologies, it will speed you up even more
    - You will have a much easier time debugging
    - You know 'best' practices
    - You know what you are doing ;)
    - I failed miserably when I trusted gpt-4 to use react (I don't know react)
- llms can speed up coding significantly
- the llm can actually handle simple systems-architecture problems
- You are very much forced to build decoupled and modular code (which is good) because the llm will have "forgotten" your specs
    - Bonus: Let the llm generate interface specs, these you can then put in the prompt if you need a specific module
- You are also very much forced to use Infrastructure-as-Code and templates, because llms can only generate text
- You will lose a lot of time if you switch back and forth between google/SoF and your llm - stick to one!
