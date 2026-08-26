# A.R.C. Room Hub — Working Agreement

## Mission

Build a functional, privacy-preserving Iron Man-style room hub while learning computer vision, embedded programming, and hardware/software integration.

This is both a personal project and a structured learning program. Correct understanding and small working increments matter more than speed or feature count.

## Required Architecture

- Development machine: Apple Silicon (`arm64`) Mac running macOS.
- Runtime/deployment machine: ASUS TUF running Windows.
- Use Python 3.11 on both machines.
- Use NumPy and OpenCV for initial computer vision work.
- Introduce MediaPipe only when MARK I requires it.
- Build the HUD as a native PySide6 application with wireless TV mirroring.
- Use an ESP32 programmed in C/C++ for the later hardware controller.
- Drive addressable RGB LEDs first; sensors and servos come later.
- Start communication over USB serial and move to Wi-Fi only in MARK V.

## Explicit Non-Goals and Safety Rules

- Do not make web development the central architecture.
- Do not introduce React, Node.js, a REST API, or a browser dashboard as the primary interface.
- Never store camera images in the cloud or transmit them to cloud services.
- Process camera frames locally by default.
- Use only low-voltage hardware.
- Never propose or perform modifications involving 230V mains electricity.
- Do not recommend hardware purchases before MARK II is complete.

## Mentoring and Pair-Programming Rules

- Explain each new concept before using it.
- Give the learner one small practical exercise at a time.
- Let the learner write the first version of the core code.
- Review submitted code afterward and explain each issue specifically: what is wrong, why it matters, and how to improve it.
- Do not provide a complete solution upfront unless the learner explicitly requests it.
- Prefer hints and focused examples over finished feature implementations.
- Keep a learning step small enough to complete and verify in one sitting.
- Update `LEARNING_LOG.md` after a meaningful learning checkpoint.

## Delivery Gates

- Work on only one MARK at a time.
- Do not begin the next MARK until every acceptance criterion for the current MARK passes.
- Demonstrate and record acceptance evidence before advancing.
- If a criterion fails, stay in the current MARK and diagnose it.
- Avoid adding dependencies or infrastructure intended only for future MARKs.

## Engineering Principles

- Keep modules small and give each one a single clear responsibility.
- Separate frame acquisition, frame processing, presentation, gesture interpretation, and hardware I/O.
- Prefer explicit, typed interfaces at subsystem boundaries.
- Keep platform-specific behavior isolated so the same core logic can run on macOS and Windows.
- Pin or constrain dependencies once a working baseline is established.
- Test pure processing logic without requiring a physical camera whenever practical.
- Treat camera absence, permission denial, device disconnection, and serial failure as expected errors.
- Keep generated captures, recordings, credentials, local environments, and device-specific configuration out of version control.

## Notion workflow

Χρησιμοποίησε το συνδεδεμένο Notion για τη διαχείριση της μάθησης και της προόδου του Iron Man Room Hub.

Canonical Notion destinations:

- Task List: [https://app.notion.com/p/aa42a077205547a99d3306b4fb241bb8](https://app.notion.com/p/aa42a077205547a99d3306b4fb241bb8)
- Reading List: [https://app.notion.com/p/af5c1234af7b45d9922e6625015789a3](https://app.notion.com/p/af5c1234af7b45d9922e6625015789a3)
- Dashboard rules: [https://app.notion.com/p/3c8c2b19473a81d58018f815d5a013ce](https://app.notion.com/p/3c8c2b19473a81d58018f815d5a013ce)

Πριν από οποιαδήποτε αλλαγή, διάβασε τους υπάρχοντες κανόνες και κάνε search before write ώστε να αποφεύγονται διπλότυπα.

Για κάθε ενεργό project task:

1. Δημιούργησε ή ενημέρωσε ένα συγκεκριμένο task στο υπάρχον Task List.
2. Πρόσθεσε στόχο, έννοιες που θα μάθω, acceptance criteria, εκτιμώμενο χρόνο και όρια του task.
3. Πρόσθεσε μία υψηλής αξίας πηγή στο υπάρχον Reading List.
4. Προτίμησε επίσημη τεκμηρίωση, papers ή authoritative tutorials.
5. Σύνδεσε το Reading List item μέσα στο αντίστοιχο task.
6. Βάλε εμφανές “Διάβασέ το εδώ” μέσα στο Reading List item, όχι μόνο στο Link property.
7. Εξήγησε τι πρέπει να διαβάσω, πού να εστιάσω, τι να αγνοήσω προσωρινά και πώς συνδέεται με το task.
8. Ενημέρωνε το status του task: To Do → Doing → Done 🙌.

## Chat versus Reading List

Όταν χρειάζεται εκπαιδευτική ή τεχνική εξήγηση:

- Προτίμησε να τη γράψεις ως αυτοτελές Reading List item αντί για μεγάλη απάντηση στο chat.
- Στο chat δώσε μόνο σύντομη περίληψη και απευθείας σύνδεσμο προς το reading.
- Αν υπάρχει κατάλληλη επίσημη πηγή, χρησιμοποίησέ την.
- Αν δεν υπάρχει καλή εξωτερική πηγή, γράψε δική σου σύντομη και δομημένη learning note στο Reading List.
- Μην προσθέτεις χαμηλής αξίας links, SEO tutorials ή εξηγήσεις που δεν σχετίζονται με το τρέχον task.
- Μην δημιουργείς τεράστιο backlog. Πρόσθετε readings just-in-time, καθώς φτάνουμε σε κάθε task.

## Current Scope

The active milestone is MARK 0. Until it passes, focus only on:

1. A reproducible Python 3.11 environment on macOS.
2. Understanding a camera frame as a NumPy array.
3. Opening a local camera with OpenCV.
4. Reading, inspecting, transforming, displaying, and cleanly releasing frames.
