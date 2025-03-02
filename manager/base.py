import ollama # type: ignore
from manager import db_manager
DB_manager = db_manager.Manager()

def perfect_generate(question, regenerate=False):
    context = []
    if regenerate == True:
        context = DB_manager.get_memory()
    system = DB_manager.get_instruction()
    options = {
        "min_p": DB_manager.get_min_p(),
        "temperature": DB_manager.get_temperature()
    }
    # model = "hf.co/SAi404/niko_second:Q4_K_M"
    model = "tinyllama"
    answer = base_generate(question, context, model, system, options)
    if DB_manager.get_history() == True and regenerate == False:
        DB_manager.set_memory(answer[1])
    return answer[0]

def short_description(text):
    instruction = "Ответь одним кратким предложением что находиться в этом предложении кратко пересказав или перечислив ключевые слова:\n"
    answer = base_generate(question=instruction+str(text))[0]
    return answer

def base_generate(question, context=[], model='tinyllama', system=None, options={'temperature': 1.5, 'min_p': 0.5}):
    answer = ollama.generate(model=model,
                            system=system,
                            prompt=question, 
                            context=context, 
                            keep_alive="50m",
                            options=options
    )
    return answer['response'], answer['context']