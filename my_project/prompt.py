# prompt.py

# Mapping of sample prompts to each of the 24 agents
# in the Legis Synapse system (19 Foundational + 5 Strategists).

AGENT_PROMPTS = [
    # ==========================================================================
    # I. Elite Squad: Strategist Agents (5)
    # ==========================================================================
    {
        "agent_name": "Precedent Analysis Agent",
        "module": "Elite Squad / Strategist",
        "purpose": "Queries the legal case database to find relevant history.",
        "sample_prompt": "Have there been any court cases in Tamil Nadu defining 'reasonable wear and tear' for rental properties?",
        "expected_action": "Triggers a query to a precedent corpus (vector DB of court cases)."
    },
    {
        "agent_name": "Compliance Verification Agent",
        "module": "Elite Squad / Strategist",
        "purpose": "Queries the statutory (legal code) database to check for compliance.",
        "sample_prompt": "Is a security deposit of ₹1,00,000 for a ₹20,000/month rent in Salem legally compliant?",
        "expected_action": "Queries statutory corpus (vector DB of laws) to verify compliance."
    },
    {
        "agent_name": "Graph Reasoning Agent",
        "module": "Elite Squad / Strategist",
        "purpose": "Performs complex logic queries on the knowledge graph.",
        "sample_prompt": "If I am late on rent, what are all the cascading consequences according to the agreement, beyond just the late fee?",
        "expected_action": "Executes a query over the document’s knowledge graph to uncover hidden relationships."
    },
    {
        "agent_name": "Argument Miner Agent",
        "module": "Elite Squad / Strategist",
        "purpose": "Proactively finds weaknesses and points of leverage for negotiation.",
        "sample_prompt": "Analyze this agreement and highlight the top three clauses where I have the most leverage to negotiate.",
        "expected_action": "Analyzes outputs from risk agents + knowledge graph to find leverage points."
    },
    {
        "agent_name": "Negotiation Strategist Agent",
        "module": "Elite Squad / Strategist",
        "purpose": "Drafts alternative, fairer clauses and suggests negotiation strategies.",
        "sample_prompt": "The security deposit is non-compliant. Please draft a polite but firm email to my landlord to get it amended.",
        "expected_action": "Generates negotiation-ready drafts using compliance + precedent outputs."
    },

    # ==========================================================================
    # II. Foundational Agents (19)
    # ==========================================================================

    # -- Module: Intake & Digitization (3) --
    {
        "agent_name": "Document Ingestion Agent",
        "module": "Intake & Digitization",
        "purpose": "Handles file uploads (PDF, DOCX, JPG).",
        "sample_prompt": "Please start the full analysis on the `lease_agreement.pdf` I've just uploaded.",
        "expected_action": "Initiates the workflow, passing the file path to downstream agents."
    },
    {
        "agent_name": "OCR Agent",
        "module": "Intake & Digitization",
        "purpose": "Extracts text from images or scanned PDFs.",
        "sample_prompt": "I only have a picture of my contract. Can you process `contract_page.jpg`?",
        "expected_action": "Uses OCR (e.g., Google Cloud Vision API) to extract text."
    },
    {
        "agent_name": "Data Cleaning Agent",
        "module": "Intake & Digitization",
        "purpose": "Removes headers, footers, and formatting noise.",
        "sample_prompt": "The extracted PDF text has headers and page numbers. Can you clean it?",
        "expected_action": "Applies rules to strip non-essential repetitive elements."
    },

    # -- Module: Core Comprehension (4) --
    {
        "agent_name": "Document Classifier Agent",
        "module": "Core Comprehension",
        "purpose": "Identifies the document type (e.g., Lease, NDA).",
        "sample_prompt": "I've uploaded a legal document, but I'm not sure what it is. Can you identify it?",
        "expected_action": "Classifies the legal document type using an LLM."
    },
    {
        "agent_name": "Clause Segmenter Agent",
        "module": "Core Comprehension",
        "purpose": "Breaks the full text into individual clauses.",
        "sample_prompt": "Please take the agreement and segment it into a list of clauses.",
        "expected_action": "Parses text into structured clauses (e.g., JSON)."
    },
    {
        "agent_name": "Entity Recognition Agent",
        "module": "Core Comprehension",
        "purpose": "Extracts key facts like names, dates, and amounts.",
        "sample_prompt": "From the document, extract the Landlord's Name, Tenant's Name, Address, and Lease Start Date.",
        "expected_action": "Extracts structured data points using NER or function calling."
    },
    {
        "agent_name": "Jargon Buster Agent",
        "module": "Core Comprehension",
        "purpose": "Defines complex legal terms in simple language.",
        "sample_prompt": "The agreement mentions 'indemnification'. What does this mean?",
        "expected_action": "Provides plain-language definitions of legal terms."
    },

    # -- Module: Deep Analysis & Simplification (3) --
    {
        "agent_name": "Clause Simplifier Agent",
        "module": "Deep Analysis & Simplification",
        "purpose": "Rewrites legal clauses into plain English.",
        "sample_prompt": "Clause 11 is confusing. Can you simplify it?",
        "expected_action": "Simplifies legalese while preserving meaning."
    },
    {
        "agent_name": "Obligations & Rights Extractor Agent",
        "module": "Deep Analysis & Simplification",
        "purpose": "Creates 'You Must Do' and 'You Can Do' lists.",
        "sample_prompt": "List the tenant’s responsibilities and rights from this agreement.",
        "expected_action": "Classifies clauses into obligations vs. entitlements."
    },
    {
        "agent_name": "High-Level Summarizer Agent",
        "module": "Deep Analysis & Simplification",
        "purpose": "Generates a one-paragraph summary of the document.",
        "sample_prompt": "I don’t have time to read all 15 pages. Summarize in one paragraph.",
        "expected_action": "Produces a concise summary of the document."
    },

    # -- Module: Initial Risk & Compliance (4) --
    {
        "agent_name": "Risk Assessor Agent",
        "module": "Initial Risk & Compliance",
        "purpose": "Flags clauses with a Red/Yellow/Green risk score.",
        "sample_prompt": "Analyze the 'Lock-in Period' clause and assign a risk score.",
        "expected_action": "Assigns risk level with reasoning."
    },
    {
        "agent_name": "Ambiguity Detector Agent",
        "module": "Initial Risk & Compliance",
        "purpose": "Finds vague phrases that could cause disputes.",
        "sample_prompt": "Check the 'Maintenance' section for vague terms.",
        "expected_action": "Highlights ambiguous or subjective wording."
    },
    {
        "agent_name": "Missing Clause Agent",
        "module": "Initial Risk & Compliance",
        "purpose": "Identifies standard clauses that are absent.",
        "sample_prompt": "Is my rental agreement missing any standard clauses?",
        "expected_action": "Compares against a checklist of standard clauses."
    },
    {
        "agent_name": "Jurisdictional Compliance Agent",
        "module": "Initial Risk & Compliance",
        "purpose": "Performs a check against jurisdiction-specific laws.",
        "sample_prompt": "Does the 15-day notice period comply with Tamil Nadu laws?",
        "expected_action": "Verifies compliance against statutory rules."
    },

    # -- Module: User Interaction (3) --
    {
        "agent_name": "Q&A Agent",
        "module": "User Interaction",
        "purpose": "Answers user-specific questions about the document.",
        "sample_prompt": "Am I allowed to have pets in the apartment?",
        "expected_action": "Performs RAG query to return a specific answer."
    },
    {
        "agent_name": "Report Generator Agent",
        "module": "User Interaction",
        "purpose": "Assembles outputs into a clean, final report.",
        "sample_prompt": "Assemble simplified clauses, risks, and summary into a final report.",
        "expected_action": "Collates outputs into a polished format."
    },
    {
        "agent_name": "Multilingual Translator Agent",
        "module": "User Interaction",
        "purpose": "Translates the final report into local languages.",
        "sample_prompt": "Translate the summary into Tamil for my parents.",
        "expected_action": "Uses translation API to localize outputs."
    },

    # -- Module: Orchestration & Control (2) --
    {
        "agent_name": "Orchestrator Agent",
        "module": "Orchestration & Control",
        "purpose": "Manages the entire workflow and agent calls.",
        "sample_prompt": "Run the full end-to-end analysis on the uploaded document.",
        "expected_action": "Triggers the sequence of agents in correct order."
    },
    {
        "agent_name": "Privacy Guard Agent",
        "module": "Orchestration & Control",
        "purpose": "Anonymizes Personally Identifiable Information (PII).",
        "sample_prompt": "Redact my Aadhaar number and bank details before analysis.",
        "expected_action": "Detects and anonymizes PII before processing."
    }
]
