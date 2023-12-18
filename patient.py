import streamlit as st

# Set the title
st.title('Patient Wait List Report')

# Center-align the entire report using CSS
st.markdown(
    """
    <style>
    .report-container {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Create a container div for the report content
st.markdown('<div class="report-container">', unsafe_allow_html=True)

# Add your report content here
st.markdown(
    """
    ## KEY INSIGHTS AND FINDINGS

    Based on the analysis of the inpatient and outpatient datasets from 2018 to 2021, here are some key insights and findings to include in your report for the Streamlit app:

    **Report: Patient Waiting List Analysis (2018-2021)**

    **1. Overall Patient Trends:**

    * **Yearly Trends:** A noticeable fluctuation in the total number of patients was observed across the years. (Specific trends based on the analysis of out_total_patients_year and in_total_patients_year data can be detailed here).
    * **Inpatient vs. Outpatient:** Distinct patterns emerged in patient numbers between inpatient and outpatient services, highlighting different demands and capacities in these areas.

    **2. Specialty-Specific Analysis:**

    * **Most Demanding Specialties:** Certain specialties consistently showed higher average patient numbers, indicating a greater demand or longer waiting times in these areas (Details based on out_avg_patients_specialty and in_avg_patients_specialty).
    * **Variations Across Specialties:** Each specialty demonstrated unique trends, suggesting the need for targeted resource allocation and management strategies.

    **3. Age Profile Distribution:**

    * **Predominant Age Groups:** The analysis revealed predominant age groups in the waiting lists, with significant differences observed in the distribution between inpatient and outpatient services (Insights based on out_total_patients_age and in_total_patients_age).
    * **Age-Specific Service Needs:** Differences in age profiles suggest varying healthcare needs and potentially different approaches required for patient care and service provision.

    **4. Key Conclusions:**

    * The analysis underscores the importance of continuous monitoring and adaptive resource management in healthcare services.
    * Special attention is needed for high-demand specialties to mitigate long waiting times and improve patient care.
    * Understanding the age-specific distribution of patients can aid in better planning and service delivery tailored to different demographic groups.

    **5. Recommendations for Future Strategies:**

    **A. Targeted Capacity Building:**

    * Allocate resources and personnel according to demand fluctuations across specialties.
    * Focus on expanding capacity in high-demand specialties with consistently high patient numbers or longer waiting times.
    * Consider implementing flexible staffing models to adapt to seasonal or unexpected surges in demand.

    **B. Streamlined Patient Flow:**

    * Implement data-driven appointment scheduling systems to optimize time slots and minimize idle time.
    * Explore telehealth opportunities for appropriate specialties to improve access and reduce in-person waiting times.
    * Investigate opportunities for triage systems to prioritize urgent cases and ensure efficient patient flow.

    **C. Age-Specific Service Tailoring:**

    * Develop dedicated programs and services catering to the specific needs of predominant age groups identified in the waiting list analysis.
    * Invest in geriatric healthcare expertise to cater to the increasing needs of the aging population.
    * Design educational materials and awareness campaigns tailored to different age groups to promote preventive care and early intervention.

    **6. Continuous Monitoring and Evaluation:**

    * Establish a system for regularly monitoring and analyzing waiting list data to track progress and identify emerging trends.
    * Utilize data insights to evaluate the effectiveness of implemented strategies and make necessary adjustments.
    * Foster a culture of data-driven decision-making to continuously improve healthcare service delivery and patient satisfaction.

    **7. Patient-Centric Approach:**

    * Implement mechanisms for collecting and incorporating patient feedback into service improvement initiatives.
    * Promote transparency and communication regarding waiting times and treatment options.
    * Focus on enhancing the overall patient experience throughout the waiting and treatment process.
    """,
    unsafe_allow_html=True,
)

# Close the container div
st.markdown('</div>', unsafe_allow_html=True)

# Display the images (page1.png and page2.png)
st.image('page 1.png', caption='Page 1', use_column_width=True)
st.image('page 2.png', caption='Page 2', use_column_width=True)
