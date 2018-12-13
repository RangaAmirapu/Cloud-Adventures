// Loading the required modules

const fs = require('fs');
const _ = require('lodash');
const yargs = require('yargs');

const notes = require('./notes.js');

const titleOptions = {
    describe: 'Title of Note',
    demand: true,
    alias: 't'
};

const bodyOptions = {
    describe: 'Body of Note',
    demand: true,
    alias: 'b'
};

//Settings for command line input

const argv = yargs
    .command('add', 'Add a new note', {
        title: titleOptions,
        body: bodyOptions
    })
    .command('list', 'List all notes')
    .command('read', 'Read a note', {
        title: titleOptions
    })
    .command('remove', 'Remove a note', {
        title: titleOptions
    })
    .help().argv;

//Getting the command

var command = process.argv[2];

//Processing the command obtained

if (command === 'add') {
    console.log('Adding Note: ', argv.title);
    var note = notes.addNote(argv.title, argv.body);
    if (note != undefined) {

        console.log(`Note created !!`);
        notes.logNote(note);
    }
    else {
        console.log('Note with same title exists');
    }

}
else if (command === 'list') {
    console.log('Getting all the notes');
    var Allnotes = notes.getAll();
    console.log(`Printing ${Allnotes.length} notes`);
    Allnotes.forEach((note) => {
        notes.logNote(note);
    });

}
else if (command === 'read') {
    console.log('Getting Note: ', argv.title)
    var note = notes.readNote(argv.title);
    if (note) {
        notes.logNote(note);
    }
    else {
        console.log('Note not found')
    }

}
else if (command === 'remove') {
    console.log('Deleting Note: ', argv.title)
    console.log(`------------------------------`);
    console.log(notes.removeNote(argv.title));

}
else {
    console.log('Command not recognised');
}
