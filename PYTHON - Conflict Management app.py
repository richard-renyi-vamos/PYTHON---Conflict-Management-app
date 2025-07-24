import datetime

class Conflict:
    def __init__(self, description, parties, severity):
        self.id = id(self)
        self.description = description
        self.parties = parties
        self.severity = severity
        self.status = "Open"
        self.created_at = datetime.datetime.now()
        self.resolution_notes = ""

    def update_status(self, new_status, notes=""):
        self.status = new_status
        self.resolution_notes = notes

    def __str__(self):
        return (f"Conflict ID: {self.id}\n"
                f"Description: {self.description}\n"
                f"Parties: {', '.join(self.parties)}\n"
                f"Severity: {self.severity}\n"
                f"Status: {self.status}\n"
                f"Created At: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"Resolution Notes: {self.resolution_notes}\n")


class ConflictManager:
    def __init__(self):
        self.conflicts = []

    def add_conflict(self, description, parties, severity):
        conflict = Conflict(description, parties, severity)
        self.conflicts.append(conflict)
        print("✅ Conflict added successfully.\n")

    def list_conflicts(self, filter_status=None):
        print("📋 Listing Conflicts:")
        for conflict in self.conflicts:
            if filter_status is None or conflict.status == filter_status:
                print(conflict)
                print("-" * 40)

    def resolve_conflict(self, conflict_id, notes):
        for conflict in self.conflicts:
            if conflict.id == conflict_id:
                conflict.update_status("Resolved", notes)
                print("🎯 Conflict resolved!\n")
                return
        print("❌ Conflict ID not found.\n")


# 🎮 Example Usage
if __name__ == "__main__":
    manager = ConflictManager()

    manager.add_conflict("Miscommunication about project deadline", ["Alice", "Bob"], "High")
    manager.add_conflict("Disagreement on design choice", ["Team A", "Team B"], "Medium")

    manager.list_conflicts()

    # Get the ID of the first conflict for demonstration
    first_conflict_id = manager.conflicts[0].id
    manager.resolve_conflict(first_conflict_id, "Held a meeting and clarified responsibilities.")

    manager.list_conflicts(filter_status="Resolved")
