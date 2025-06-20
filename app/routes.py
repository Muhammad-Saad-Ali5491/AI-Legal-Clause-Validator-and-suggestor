import streamlit as st
from app.utils import (
    extract_text,
    is_legal_document,
    segment_clauses,
    classify_clause,
    detect_document_type,
    suggest_clause,
    generate_docx_report
)

def render_app():
    st.set_page_config(page_title="🧾 AI Legal Validator", layout="wide")
    st.markdown("<h1 style='text-align: center;'>🧾 AI Legal Clause Validator & Suggestion Tool</h1>", unsafe_allow_html=True)
    st.markdown("Upload a **legal contract** (.pdf or .docx), and get intelligent clause classification and rewrite suggestions powered by LegalBERT & Gemini.")

    uploaded_file = st.file_uploader("📁 Upload Legal Document", type=["pdf", "docx"])

    if uploaded_file:
        with st.spinner("🔍 Reading file..."):
            text = extract_text(uploaded_file)

        if not is_legal_document(text):
            st.error("❌ The uploaded file does not appear to be a legal document.")
            return

        with st.spinner("✂️ Segmenting clauses..."):
            clauses = segment_clauses(text)

        if clauses:
            st.success(f"✅ Detected {len(clauses)} clauses. Classifying...")

            result_data = []
            label_conf_list = []

            progress = st.progress(0)
            for i, clause in enumerate(clauses):
                label, confidence = classify_clause(clause)
                label_conf_list.append((label, confidence))
                suggestion = suggest_clause(clause, label)

                result_data.append({
                    "text": clause,
                    "label": label,
                    "confidence": confidence,
                    "suggestion": suggestion
                })

                progress.progress((i+1)/len(clauses))

            document_type = detect_document_type(label_conf_list)
            st.markdown(f"📄 **Predicted Document Type**: `{document_type}`")
            st.markdown(f"🔢 **Total Clauses**: `{len(clauses)}`")

            for idx, data in enumerate(result_data):
                with st.expander(f"📌 Clause {idx+1} — {data['label']} (Confidence: {data['confidence']:.2f})"):
                    st.markdown(f"<b>🔹 Original:</b><br>{data['text']}", unsafe_allow_html=True)
                    st.markdown(f"<b>🔁 Suggested Rewrite:</b><br><i>{data['suggestion']}</i>", unsafe_allow_html=True)

            st.success("✅ All clauses analyzed!")

            docx_data = generate_docx_report(result_data)
            st.download_button("📥 Download DOCX Report", docx_data, file_name="AI_Clause_Report.docx")

        else:
            st.warning("⚠️ No clauses detected in the document.")
