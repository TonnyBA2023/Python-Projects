from datetime import datetime


class Patient:

    def __init__(
        self,
        patient_id,
        name,
        age,
        gender,
        diagnosis
    ):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.diagnosis = diagnosis
        self.admission_date = datetime.now()

    def display_details(self):

        print("\nPATIENT DETAILS")
        print("-" * 40)

        print(f"Patient ID: {self.patient_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Diagnosis: {self.diagnosis}")
        print(
            f"Admission Date: "
            f"{self.admission_date.strftime('%Y-%m-%d')}"
        )


class Doctor:

    def __init__(
        self,
        doctor_id,
        name,
        specialization
    ):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization

    def display_details(self):

        print("\nDOCTOR DETAILS")
        print("-" * 40)

        print(f"Doctor ID: {self.doctor_id}")
        print(f"Name: {self.name}")
        print(
            f"Specialization: "
            f"{self.specialization}"
        )


class Appointment:

    def __init__(
        self,
        appointment_id,
        patient,
        doctor,
        appointment_date
    ):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.appointment_date = appointment_date

    def display_details(self):

        print("\nAPPOINTMENT")
        print("-" * 40)

        print(
            f"Appointment ID: "
            f"{self.appointment_id}"
        )

        print(
            f"Patient: "
            f"{self.patient.name}"
        )

        print(
            f"Doctor: "
            f"{self.doctor.name}"
        )

        print(
            f"Date: "
            f"{self.appointment_date}"
        )


class HospitalManagementSystem:

    def __init__(self):

        self.patients = []
        self.doctors = []
        self.appointments = []

    def register_patient(
        self,
        name,
        age,
        gender,
        diagnosis
    ):

        patient_id = len(self.patients) + 1

        patient = Patient(
            patient_id,
            name,
            age,
            gender,
            diagnosis
        )

        self.patients.append(patient)

        print(
            f"\nPatient registered successfully."
            f" ID: {patient_id}"
        )

    def add_doctor(
        self,
        name,
        specialization
    ):

        doctor_id = len(self.doctors) + 1

        doctor = Doctor(
            doctor_id,
            name,
            specialization
        )

        self.doctors.append(doctor)

        print(
            f"\nDoctor added successfully."
            f" ID: {doctor_id}"
        )

    def schedule_appointment(
        self,
        patient_id,
        doctor_id,
        appointment_date
    ):

        patient = None
        doctor = None

        for p in self.patients:
            if p.patient_id == patient_id:
                patient = p

        for d in self.doctors:
            if d.doctor_id == doctor_id:
                doctor = d

        if patient is None:
            print("Patient not found.")
            return

        if doctor is None:
            print("Doctor not found.")
            return

        appointment_id = (
            len(self.appointments) + 1
        )

        appointment = Appointment(
            appointment_id,
            patient,
            doctor,
            appointment_date
        )

        self.appointments.append(
            appointment
        )

        print(
            "\nAppointment scheduled "
            "successfully."
        )

    def view_patients(self):

        if not self.patients:
            print("\nNo patients found.")
            return

        for patient in self.patients:
            patient.display_details()

    def view_doctors(self):

        if not self.doctors:
            print("\nNo doctors found.")
            return

        for doctor in self.doctors:
            doctor.display_details()

    def view_appointments(self):

        if not self.appointments:
            print(
                "\nNo appointments found."
            )
            return

        for appointment in self.appointments:
            appointment.display_details()

    def search_patient(self, name):

        results = []

        for patient in self.patients:

            if (
                name.lower()
                in patient.name.lower()
            ):
                results.append(patient)

        return results

    def hospital_statistics(self):

        print("\nHOSPITAL REPORT")
        print("=" * 50)

        print(
            f"Total Patients: "
            f"{len(self.patients)}"
        )

        print(
            f"Total Doctors: "
            f"{len(self.doctors)}"
        )

        print(
            f"Total Appointments: "
            f"{len(self.appointments)}"
        )


def display_menu():

    print("\n")
    print("=" * 50)
    print("HOSPITAL MANAGEMENT SYSTEM")
    print("=" * 50)

    print("1. Register Patient")
    print("2. Add Doctor")
    print("3. Schedule Appointment")
    print("4. View Patients")
    print("5. View Doctors")
    print("6. View Appointments")
    print("7. Search Patient")
    print("8. Hospital Statistics")
    print("9. Exit")


def main():

    hospital = HospitalManagementSystem()

    while True:

        display_menu()

        choice = input(
            "\nEnter your choice: "
        )

        if choice == "1":

            name = input(
                "Patient Name: "
            )

            age = int(
                input("Age: ")
            )

            gender = input(
                "Gender: "
            )

            diagnosis = input(
                "Diagnosis: "
            )

            hospital.register_patient(
                name,
                age,
                gender,
                diagnosis
            )

        elif choice == "2":

            name = input(
                "Doctor Name: "
            )

            specialization = input(
                "Specialization: "
            )

            hospital.add_doctor(
                name,
                specialization
            )

        elif choice == "3":

            patient_id = int(
                input(
                    "Patient ID: "
                )
            )

            doctor_id = int(
                input(
                    "Doctor ID: "
                )
            )

            appointment_date = input(
                "Appointment Date: "
            )

            hospital.schedule_appointment(
                patient_id,
                doctor_id,
                appointment_date
            )

        elif choice == "4":

            hospital.view_patients()

        elif choice == "5":

            hospital.view_doctors()

        elif choice == "6":

            hospital.view_appointments()

        elif choice == "7":

            keyword = input(
                "Patient Name: "
            )

            results = (
                hospital.search_patient(
                    keyword
                )
            )

            if not results:
                print(
                    "No patient found."
                )

            for patient in results:
                patient.display_details()

        elif choice == "8":

            hospital.hospital_statistics()

        elif choice == "9":

            print(
                "\nSystem Closed."
            )

            break

        else:

            print(
                "Invalid option."
            )


if __name__ == "__main__":
    main()
