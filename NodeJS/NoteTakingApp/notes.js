const fs = require('fs');

var fetchNotes = () => {
    try {
        var notesString = fs.readFileSync('notes-data.json');
        return JSON.parse(notesString);
    }
    catch (e) {
        return [];
    }
};

var saveNotes = (notes) => {
    fs.writeFileSync('notes-data.json', JSON.stringify(notes));
}

var addNote = (title, body) => {
    var notes = fetchNotes();
    var note = {
        title,
        body
    };

var duplicateNotes = notes.filter((note) => note.title === title);

    if (duplicateNotes.length === 0) {
        notes.push(note);
        saveNotes(notes);
        return note;
    }
};

var listAll = () => {
    return fetchNotes();
};

var readNote = (title) => {
    var notes = fetchNotes();
    var filteredNotes = notes.filter((note) => note.title === title);
    return filteredNotes[0];

};

var removeNote = (title) => {
    var notes = fetchNotes();
    var filteredNotes = notes.filter((note) => note.title !== title);
    if (filteredNotes.length === notes.length) {
        return `No note with title: ${title}`;
    }
    else {
        saveNotes(filteredNotes);
        return `Deleted note: ${title}`; 
    }
    
}

var logNote = (note) =>
{
    console.log(`------------------------------`);
    console.log(`Title: ${note.title}`);
    console.log(`Body: ${note.body}`);
    console.log(`------------------------------`);
}


module.exports = {
    addNote: addNote,
    getAll: listAll,
    readNote,
    removeNote,
    logNote
}