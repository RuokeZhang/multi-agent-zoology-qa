```python
import random

ZOOLOGY_CORPUS = [
    {
        "title": "African Elephant",
        "taxonomy": "Loxodonta africana",
        "facts": "Largest land mammal, matriarchal social structure.",
        "conservation": "Vulnerable (IUCN).",
    },
    {
        "title": "Bald Eagle",
        "taxonomy": "Haliaeetus leucocephalus",
        "facts": "Apex predator, sexual dimorphism in size.",
        "conservation": "Least Concern.",
    },
]


class RouterAgent:
    CATEGORIES = ["taxonomy", "behavior", "ecology", "physiology", "conservation"]

    def route(self, question: str) -> str:
        # TODO: Implement robust intent classification and routing
        lower_q = question.lower()
        for cat in self.CATEGORIES:
            if cat in lower_q:
                return f"{cat}_expert"
        return "general_expert"


class ZoologyKnowledgeAgent:
    def retrieve(self, question: str):
        # TODO: Replace with real RAG retrieval over curated zoology corpus
        return random.sample(ZOOLOGY_CORPUS, k=min(1, len(ZOOLOGY_CORPUS)))

    def answer(self, question: str, image_hint=None):
        # TODO: Generate grounded answers with citations from retrieved docs
        docs = self.retrieve(question)
        sources = [doc["title"] for doc in docs]
        hint = f" Image hint suggests: {image_hint}." if image_hint else ""
        answer = f"(Stub) Answer about '{question}'.{hint} Based on: {', '.join(sources)}."
        return answer, sources


class ClarifierAgent:
    def check(self, question: str):
        # TODO: Detect ambiguity and generate clarifying questions
        if "it" in question.lower():
            return ["Which species are you referring to?"]
        return []


class ImageHintAgent:
    def suggest_species(self, image_url: str):
        # TODO: Call real image classifier API; return candidate species
        return f"StubSpeciesFrom({image_url})"


class CurriculumAgent:
    def rewrite(self, answer: str, age_level: str):
        # TODO: Adapt language complexity by age level
        return f"[{age_level}] {answer}"


class TerminologyAgent:
    def glossary(self, question: str):
        # TODO: Extract terms and provide definitions from zoology glossary
        terms = []
        for term in ["endothermic", "keystone species", "sexual dimorphism"]:
            if term in question.lower():
                terms.append({"term": term, "definition": "(stub) definition"})
        return terms


class SessionMemoryAgent:
    def __init__(self):
        self.memory = {}

    def remember(self, session_id: str, item: str):
        # TODO: Add richer context tracking with TTL
        self.memory.setdefault(session_id, []).append(item)
        self.memory[session_id] = self.memory[session_id][-5:]

    def get_context(self, session_id: str):
        return self.memory.get(session_id, [])
```
